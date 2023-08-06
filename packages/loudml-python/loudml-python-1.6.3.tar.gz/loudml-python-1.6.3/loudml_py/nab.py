import csv
from tqdm import tqdm
from functools import partial
import urllib
import io
import os
import asyncio
import aiohttp
import async_timeout

from loudml_py.misc import (
    make_ts,
)

g_sem = asyncio.Semaphore(10)

g_base_url = 'https://raw.githubusercontent.com/{}'.format(
    'numenta/NAB/master/data/')

g_labels_url = 'https://raw.githubusercontent.com/{}'.format(
    'numenta/NAB/master/labels/combined_windows.json')

g_urls = [
    'artificialNoAnomaly/art_daily_no_noise.csv',
    'artificialNoAnomaly/art_daily_perfect_square_wave.csv',
    'artificialNoAnomaly/art_daily_small_noise.csv',
    'artificialNoAnomaly/art_flatline.csv',
    'artificialNoAnomaly/art_noisy.csv',
    'artificialWithAnomaly/art_daily_flatmiddle.csv',
    'artificialWithAnomaly/art_daily_jumpsdown.csv',
    'artificialWithAnomaly/art_daily_jumpsup.csv',
    'artificialWithAnomaly/art_daily_nojump.csv',
    'artificialWithAnomaly/art_increase_spike_density.csv',
    'artificialWithAnomaly/art_load_balancer_spikes.csv',
    'realAWSCloudwatch/ec2_cpu_utilization_24ae8d.csv',
    'realAWSCloudwatch/ec2_cpu_utilization_53ea38.csv',
    'realAWSCloudwatch/ec2_cpu_utilization_5f5533.csv',
    'realAWSCloudwatch/ec2_cpu_utilization_77c1ca.csv',
    'realAWSCloudwatch/ec2_cpu_utilization_825cc2.csv',
    'realAWSCloudwatch/ec2_cpu_utilization_ac20cd.csv',
    'realAWSCloudwatch/ec2_cpu_utilization_c6585a.csv',
    'realAWSCloudwatch/ec2_cpu_utilization_fe7f93.csv',
    'realAWSCloudwatch/ec2_disk_write_bytes_1ef3de.csv',
    'realAWSCloudwatch/ec2_disk_write_bytes_c0d644.csv',
    'realAWSCloudwatch/ec2_network_in_257a54.csv',
    'realAWSCloudwatch/ec2_network_in_5abac7.csv',
    'realAWSCloudwatch/elb_request_count_8c0756.csv',
    'realAWSCloudwatch/grok_asg_anomaly.csv',
    'realAWSCloudwatch/iio_us-east-1_i-a2eb1cd9_NetworkIn.csv',
    'realAWSCloudwatch/rds_cpu_utilization_cc0c53.csv',
    'realAWSCloudwatch/rds_cpu_utilization_e47b3b.csv',
    'realKnownCause/ambient_temperature_system_failure.csv',
    'realKnownCause/cpu_utilization_asg_misconfiguration.csv',
    'realKnownCause/ec2_request_latency_system_failure.csv',
    'realKnownCause/machine_temperature_system_failure.csv',
    'realKnownCause/nyc_taxi.csv',
    'realKnownCause/rogue_agent_key_hold.csv',
    'realKnownCause/rogue_agent_key_updown.csv',
]


async def download_file(session, url):
    try:
        async with g_sem:  # max running in parallel
            with async_timeout.timeout(10):
                async with session.get(url) as remotefile:
                    if remotefile.status == 200:
                        data = await remotefile.read()
                        return None, data
                    else:
                        return remotefile.status, None
    except Exception as e:
        return e, None


async def _load_url(
    loud, bucket_name, batch_size, from_date, session, url,
):
    global g_base_url
    global g_urls

    from_ts = make_ts(from_date)
    url = urllib.parse.urljoin(g_base_url, url)
    error, data = await download_file(session, url)
    content = io.StringIO(data.decode('utf-8'))
    csv_reader = csv.reader(content, delimiter=',')
    next(csv_reader, None)  # skip the header
    tag_val = os.path.basename(os.path.splitext(url)[0])

    delta = None
    points = []
    for row in csv_reader:
        ts = make_ts(row[0])
        if delta is None:
            delta = ts - from_ts

        ts -= delta
        val = float(row[1])
        point = {
            'timestamp': str(ts),
            'value': val,
            'tags': {
                'file': tag_val,
            }
        }
        points.append(point)
        if len(points) >= batch_size:
            await loud.async_write_points(
                bucket_name, points, verbose=False)
            points.clear()

    if len(points):
        await loud.async_write_points(bucket_name, points, verbose=False)


async def load_nab(loud, bucket_name, batch_size, from_date):
    global g_urls

    load = partial(_load_url, loud, bucket_name, batch_size, from_date)
    pbar = tqdm(total=len(g_urls))

    async def load_and_update(session, url):
        await load(session, url)
        pbar.update()

    con = aiohttp.TCPConnector(limit=10)
    loop = asyncio.get_event_loop()
    async with aiohttp.ClientSession(loop=loop, connector=con) as session:
        tasks = [
            asyncio.ensure_future(load_and_update(session, url))
            for url in g_urls
        ]
        return await asyncio.gather(*tasks)
