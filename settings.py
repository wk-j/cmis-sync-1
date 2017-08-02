SOURCE_REPOSITORY_URL = 'http://192.168.0.20:8080/alfresco/cmisatom'  # Alfresco 4.0
#SOURCE_REPOSITORY_URL = 'http://192.168.0.20:8080/alfresco/api/-default-/public/cmis/versions/1.0/atom'  # Alfresco 4.0
SOURCE_USERNAME = 'admin'
SOURCE_PASSWORD = 'admin'

TARGET_REPOSITORY_URL = 'http://192.168.0.109:8080/alfresco/cmisatom'  # OpenCMIS InMemory 0.8.0 Snapshot
#TARGET_REPOSITORY_URL = 'http://192.168.0.109:8000/alfresco/api/-default-/public/cmis/versions/1.0/atom'  # OpenCMIS InMemory 0.8.0 Snapshot
TARGET_USERNAME = 'admin'
TARGET_PASSWORD = 'admin'
TARGET_ROOT = '/cmis-sync'

# The number of seconds to wait before polling for changes in the source
POLL_INTERVAL = 10
