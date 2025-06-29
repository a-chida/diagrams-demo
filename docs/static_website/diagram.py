from diagrams import Diagram, Edge
from diagrams.aws.network import Route53
from diagrams.aws.security import CertificateManager
from diagrams.aws.storage import S3
from diagrams.aws.network import CloudFront
from diagrams.aws.general import User

with Diagram("Static Website Hosting on AWS", show=False, filename="static-website-aws"):
    user = User("Website Visitor")
    dns = Route53("Domain")
    cert = CertificateManager("SSL Certificate")
    cdn = CloudFront("CDN")
    bucket = S3("Static Website Bucket")

    user >> dns >> Edge(label="HTTPS") >> cdn >> bucket
    cdn >> cert