import logging
from time import sleep
from .structure import Pipeline
from .stats import compute_stage_status, compute_pipe_sizes, compute_throughput
import signal

def default_report_callback(throughputs: dict, pipe_sizes: dict):
    for key, value in throughputs.items():
        logging.debug(f"stage {key} has throughput {value}")
    
    for key, value in pipe_sizes.items():
        logging.debug(f"pipe {key} has {value}")


def run_forever(pipeline: Pipeline, report_freq=10, report_callback=None, timeout=1):
    report_callback = report_callback or default_report_callback

    pipeline.start()

    def cleanup(signum, frame):
        logging.info("SIGTERM triggered termination")

        logging.info("Stopping pipeline stages")
        pipeline.stop(timeout=timeout)
        logging.info("Joining terminated stages")
        pipeline.join()
        exit(0)

    signal.signal(signal.SIGTERM, cleanup)

    try:
        sleep(report_freq)
        alive = compute_stage_status(pipeline)

        while all(alive):
            alive = compute_stage_status(pipeline)
            throughputs = compute_throughput(pipeline)
            pipe_sizes = compute_pipe_sizes(pipeline)
            report_callback(throughputs, pipe_sizes)
            sleep(report_freq)

    except KeyboardInterrupt:
        logging.info("SIGINT triggered termination")

        logging.info("Stopping pipeline stages")
        pipeline.stop(timeout=timeout)

        logging.info("Joining terminated stages")
        pipeline.join()

