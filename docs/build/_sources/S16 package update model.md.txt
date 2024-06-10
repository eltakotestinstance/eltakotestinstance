# S16 package update model

```mermaid
flowchart TD
   nSystem([normal system]) 
   nSystem-->connect["connect to 
   the package 
   managment server"]
   connect-->successConnect{successful}
   successConnect-->|yes|checkSSL["check ssl certificate
   of connection"]
   successConnect-->|no|waitConnect[wait for x seconds]:::wait
   waitConnect-->maxTries{"max number of
   tries reached"}
   maxTries-->|no|connect
   maxTries-->|yes|errorLog(["error log/
   message to app"]):::failed
   errorLog-->consent{"has user consented
   for diagnostic data"}:::failed
   consent-->sendDiagData(["send dignostic
   data"]):::failed
   checkSSL-->validSSL{valid}
   validSSL-->|yes|authenticate[authenticate]
   validSSL--> |no|errorLog
   authenticate-->authSuccess{successful}
   authSuccess-->|yes|updateRepo[("update package
    repository")]
   authSuccess-->|no|errorLog
  updateRepo-->successRepo{successful}
  successRepo-->|yes|newPackages{"new Packages
  availible"}
  successRepo-->|no|errorLog
  newPackages-->|no|waitForPackages["wait for 
  x hours/days"]:::wait
  waitForPackages-->connect
  newPackages-->|yes|notify["notify the user
  that updates
  are availible"]
  notify-->prioUpdate{priority Update}
  prioUpdate-->|no|waitForUser["wait for user to
  initiate update"]:::wait
  waitForUser-->updatePackages[(update packages)]
  prioUpdate-->|yes|updatePackages
  updatePackages-->successPackages{successful}
  successPackages-->|yes|needMigration{need migration}
  successPackages-->|no|revertUpdates[revert updates]:::failed
  revertUpdates-->errorLog
  needMigration-->|yes|backup["backup 
  migration data"]
  needMigration-->|no|reload
  backup-->pUMigration["post update
  migration(db)"]
  pUMigration-->successMigration{successful}
  successMigration-->|yes|reload[reload services]
  successMigration-->|no|revertMigration["revert migration
  data"]:::failed
  revertMigration-->revertUpdates
  reload-->successReload{successful}
  successReload-->|no|migrationMade{"migration
  cahnges made"}
  migrationMade-->|yes|revertMigration
  migrationMade-->|no|revertUpdates
  successReload-->|yes|endSuccess(["log success/
  message to app"]):::success
  classDef success fill:#006400
  classDef failed fill:#cd0000
  classDef wait fill:#ffd700,color:#000000
```
