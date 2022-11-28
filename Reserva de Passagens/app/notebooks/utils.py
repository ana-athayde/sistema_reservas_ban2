def remove_csrf(d):
    return {k: v for k, v in d.items() if k != 'csrf_token'}
