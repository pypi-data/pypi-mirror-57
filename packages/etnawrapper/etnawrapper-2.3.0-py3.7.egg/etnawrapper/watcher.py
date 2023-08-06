#!/usr/bin/env python
"""
Period check of ETNA's services
"""
from datetime import datetime
import time
import typing

import requests


try:
    import prometheus_client
    PROMETHEUS_SUPPORT = True
except ImportError:
    print('no prometheus')
    PROMETHEUS_SUPPORT = False


SLEEP_DURATION = 10  # Seconds between two loops
URLS = [
    "https://rendu-git.etna-alternance.net",
    "https://intra-api.etna-alternance.net",
]


def _configure_url(url: str, timeout: int, auth: bool) -> dict:
    """Add metadata to target url."""
    return {
        'url': url,
        'timeout': timeout,
        'auth': auth,
    }


def get_targets(urls) -> typing.List[dict]:
    """Fetch the URLs to target."""
    _urls = urls
    return [_configure_url(url, 5, False) for url in _urls]


def process_url(target: dict):
    """Try to reach the target url.

    .. code::javascript

        {
            "failed": "bool",
            "duration": "int", // requests duration in ms
            "method": "str",
            "message": "str",
            "url": "str",
            "at": "datetime.datetime",
        }
    """
    since = datetime.now()
    duration = since - since
    try:
        requests.head(target['url'], timeout=target['timeout'])
    except requests.exceptions.BaseHTTPError as err:
        duration = datetime.now() - since
        # TODO: Variabilize method management
        return {
            'failed': True,
            'duration': duration.microseconds,
            'method': 'HEAD',
            'message': str(err),
            'url': target['url'],
            'at': since,
        }
    result = {
        'failed': False,
        'duration': duration.microseconds,
        'method': 'HEAD',
        'message': 'success',
        'url': target['url'],
        'at': since,
    }
    return result


def _display_results(result: dict):
    """Pretty print request results."""
    _at = result['at']
    method = result['method']
    success = 'OK' if not result['failed'] else 'KO'
    print(f"Request @{_at}: {success} {method} - {result['url']}")


def main_loop(targets):
    """Main processing function."""

    _post_process = [_display_results]

    while True:
        results = [process_url(target) for target in targets]
        for hook in _post_process:
            _ = [hook(result) for result in results]
        time.sleep(SLEEP_DURATION)


def main():
    """Script entrypoint."""
    targets = get_targets(URLS)
    main_loop(targets)


if __name__ == '__main__':
    main()
