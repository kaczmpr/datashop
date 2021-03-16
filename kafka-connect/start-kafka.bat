@ECHO OFF
ECHO echo %cd%
ECHO ==========================
ECHO Go to kafka directory
ECHO ==========================
CD /D D:\kafka
ECHO echo %cd%
ECHO ==========================
ECHO STARTING ZOOKEEPER
ECHO ==========================
start .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
timeout 15
ECHO ==========================
ECHO STARTING KAFKA SERVER
ECHO ==========================
start .\bin\windows\kafka-server-start.bat .\config\server.properties
CD /D D:\PycharmProjects\datashop
ECHO END