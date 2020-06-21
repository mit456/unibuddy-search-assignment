"use strict"

// Required modules
require("dotenv").config()
const config = require("./config/web")
const logger = config.logger

// .env contains a key NODE_PROCESS_TYPE
const PROCESS_TYPE = process.env.NODE_PROCESS_TYPE

// In future we mayrequired worker node process
// beside node serves as web server.
if (PROCESS_TYPE === "web") {
  require("./web")
  logger.log("info", "Starting %s process", PROCESS_TYPE, {pid: process.pid})
} else if (PROCESS_TYPE === "worker") {
  logger.log("info", "Starting %s process", PROCESS_TYPE, {pid: process.pid})
} else {
  throw new Error("%s is unsupported process type. Use one of web or worker", PROCESS_TYPE)
}
