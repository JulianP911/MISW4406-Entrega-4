bucketLocation = {
    "com": "us-east-1",
    "co": "us-west-1",
    "br": "sa-east-1",
    "eu": "eu-west-1",
    "default": "us-east-1",
}


def get_bucket_location(domain):
    if domain is not None:
        domain_name = domain.split("/")
        end_domain = domain_name[0].split(".")[-1]
    match end_domain:
        case "com":
            return bucketLocation["com"]
        case "co":
            return bucketLocation["co"]
        case "br":
            return bucketLocation["br"]
        case "eu":
            return bucketLocation["eu"]
        case _:
            return bucketLocation["default"]
