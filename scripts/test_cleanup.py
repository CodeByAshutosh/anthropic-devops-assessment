import unittest
from unittest.mock import MagicMock, patch
from cleanup_volumes import cleanup_unused_volumes

class TestCleanupScript(unittest.TestCase):

    @patch('boto3.resource')
    def test_cleanup_dry_run(self, mock_boto3):
        """Test that dry run does not call the delete method on volumes."""
        mock_ec2 = MagicMock()
        mock_boto3.return_value = mock_ec2
        
        # Mock an available volume
        mock_volume = MagicMock()
        mock_volume.id = 'vol-12345'
        mock_ec2.volumes.filter.return_value = [mock_volume]
        
        # Run cleanup in dry run mode
        cleanup_unused_volumes(dry_run=True)
        
        # Assert delete was NOT called
        mock_volume.delete.assert_not_called()

    @patch('boto3.resource')
    def test_cleanup_execution(self, mock_boto3):
        """Test that execution mode correctly calls the delete method."""
        mock_ec2 = MagicMock()
        mock_boto3.return_value = mock_ec2
        
        mock_volume = MagicMock()
        mock_volume.id = 'vol-67890'
        mock_ec2.volumes.filter.return_value = [mock_volume]
        
        # Run cleanup in execution mode
        cleanup_unused_volumes(dry_run=False)
        
        # Assert delete WAS called
        mock_volume.delete.assert_called_once()

if __name__ == '__main__':
    unittest.main()