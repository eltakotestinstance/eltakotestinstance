´´´mermaid
flowchart LR
   nSystem([normal system]) 
   nSystem-->connect["connect to 
   the package 
   managment server"]
   connect-->successConnect{successful}
   successConnect-->|yes|checkSSL["check ssl certificate
   of connection"]
   successConnect-->|no|waitConnect[wait for x seconds]
   waitConnect-->maxTries{"max number of
   tries reached"}
   maxTries-->|no|connect
   maxTries-->|yes|errorLog(["error log/
   message to app"])
   errorLog-->consent{"has user consented
   for diagnostic data"}
   consent-->sendDiagData(["send dignostic
   data"])
   checkSSL-->validSSL{valid}
   validSSL-->authenticate[authenticate]
   authenticate-->authSuccess{successful}
   authSuccess-->|yes|updateRepo[("update package
    repository")]
  updateRepo-->successRepo{successful}
  successRepo-->|yes|newPackages{"new Packages
  availible"}
  newPackages-->|no|waitForPackages["wait for 
  x hours/days"]
  waitForPackages-->connect
  newPackages-->|yes|notify["notify the user
  that updates
  are availible"]
  notify-->prioUpdate{priority Update}
  prioUpdate-->|no|waitForUser["wait for user to
  initiate update"]
  waitForUser-->updatePackages[(update packages)]
  prioUpdate-->|yes|updatePackages
  updatePackages-->successPackages{successful}
  successPackages-->|yes|needMigration{need migration}
  successPackages-->|no|revertUpdates[revert updates]
  revertUpdates-->errorLog
  needMigration-->|yes|backup["backup 
  migration data"]
  needMigration-->|no|reload
  backup-->pUMigration["post update
  migration(db)"]
  pUMigration-->successMigration{successful}
  successMigration-->|yes|reload[reload services]
  successMigration-->|no|revertMigration["revert migration
  data"]
  revertMigration-->revertUpdates
  reload-->successReload{successful}
  successReload-->migrationMade{"migration
  cahnges made"}
  migrationMade-->|yes|revertMigration
  migrationMade-->|no|revertUpdates
  successReload-->|yes|endSuccess(["log success/
  message to app"])

´´´
