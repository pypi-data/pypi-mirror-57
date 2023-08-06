import unittest

from checkov.terraform.checks.resource.aws.S3PublicACL import check
from checkov.terraform.models.enums import CheckResult


class TestS3PublicACL(unittest.TestCase):

    def test_failure(self):
        resource_conf = {"region": ["us-west-2"],
                         "bucket": ["my_bucket"],
                         "acl": ["public-read"],
                         "force_destroy": [True],
                         "tags": [{"Name": "my-bucket"}],
                         }
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.FAILURE, scan_result)

    def test_success(self):
        resource_conf = {"region": ["us-west-2"],
                         "bucket": ["my_bucket"],
                         "force_destroy": [True],
                         "tags": [{"Name": "my-bucket"}]
                         }
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.SUCCESS, scan_result)


if __name__ == '__main__':
    unittest.main()
