from diagrams import Diagram, Edge
from diagrams.aws.network import Route53, CloudFront
from diagrams.aws.security import CertificateManager, WAF
from diagrams.aws.storage import S3
from diagrams.aws.general import User

with Diagram("Static Website Hosting on AWS", show=False, filename="static-website-aws"):
    user = User("Website Visitor")
    dns = Route53("Domain")
    cert = CertificateManager("SSL Certificate")
    cdn = CloudFront("CDN")
    waf = WAF("WAF")
    bucket = S3("Origin Bucket")

    user >> dns >> Edge(label="HTTPS") >> cdn >> waf >> bucket
    cdn >> cert