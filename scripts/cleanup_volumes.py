import boto3
import logging
import sys

# Setup logging 
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def cleanup_unused_volumes(dry_run=True):
    """Finds and deletes unattached AWS EBS volumes."""
    try:
        ec2 = boto3.resource('ec2')
        # Filter for 'available' volumes (not attached to any instance) 
        volumes = ec2.volumes.filter(Filters=[{'Name': 'status', 'Values': ['available']}])
        
        for volume in volumes:
            if dry_run:
                logging.info(f"[DRY RUN] Would delete unused volume: {volume.id}")
            else:
                logging.info(f"Deleting unused volume: {volume.id}")
                volume.delete()
    except Exception as e:
        logging.error(f"Error during cleanup: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Configurable via a simple flag for safety [cite: 126]
    EXECUTE_DELETION = False # Set to True to actually delete
    cleanup_unused_volumes(dry_run=not EXECUTE_DELETION)