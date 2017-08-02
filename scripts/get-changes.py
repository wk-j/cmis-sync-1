from cmislib.model import CmisClient, Document
import settings
import sys

def dumpRepoHeader(repo, label):
    print "=================================="
    print "%s repository info:" % label
    print "----------------------------------"
    print "    Name: %s" % repo.name
    print "      Id: %s" % repo.id
    print "  Vendor: %s" % repo.info['vendorName']
    print " Version: %s" % repo.info['productVersion']
    print "----------------------------------"

def sync():
    # Connect to the source repo
    sourceClient = CmisClient(settings.SOURCE_REPOSITORY_URL,
                          settings.SOURCE_USERNAME,
                          settings.SOURCE_PASSWORD)
    sourceRepo = sourceClient.defaultRepository
    dumpRepoHeader(sourceRepo, "SOURCE")

    # Make sure it supports changes, bail if it does not
    if sourceRepo.getCapabilities()['Changes'] == None:
        print "Source repository does not support changes:" + sourceRepo.getCapabilities()['Changes']
        sys.exit(-1)
    latestChangeToken = sourceRepo.info['latestChangeLogToken']
    print "Latest change token: %s" % latestChangeToken

    # Connect to the target repo
    targetClient = CmisClient(settings.TARGET_REPOSITORY_URL,
                          settings.TARGET_USERNAME,
                          settings.TARGET_PASSWORD)
    targetRepo = targetClient.defaultRepository
    dumpRepoHeader(targetRepo, "TARGET")
    print "    Path: %s" % settings.TARGET_ROOT
    
    # Get last token synced from savefile
    # Using the repository IDs so that you can use this script against
    # multiple source-target pairs and it will remember where you are
    syncKey = "%s><%s" % (sourceRepo.id, targetRepo.id)
    lastChangeSynced = {}
    changeToken = None

    '''
    if (os.path.exists(SAVE_FILE)):
        lastChangeSynced = pickle.load(open(SAVE_FILE, "rb" ))
        if lastChangeSynced.has_key(syncKey):
            print "Last change synced: %s" % lastChangeSynced[syncKey]
            changeToken = lastChangeSynced[syncKey]
        else:
            print "First sync..."
    else:
        print "First sync..."
    '''

    if changeToken == latestChangeToken:
        print "No changes since last sync so no work to do"
        return

    # Ask the source repo for changes
    changes = None
    if changeToken != None:
        changes = sourceRepo.getContentChanges(changeLogToken=changeToken)
    else:
        changes = sourceRepo.getContentChanges()

    # Process each change
    for change in changes:
        if change.changeType == 'created' or change.changeType == 'updated':
            processChange(change, sourceRepo, targetRepo)

    lastChangeSynced[syncKey] = latestChangeToken

    '''
    pickle.dump(lastChangeSynced, open(SAVE_FILE, "wb"))
    '''
    print "last change sync %s" % lastChangeSynced

    return


def processChange (change, sourceRepo, targetRpo): 
    print "%s %s" % (change.id, change.changeType)


sync()