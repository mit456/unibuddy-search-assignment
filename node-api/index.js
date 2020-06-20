"use strict"

require("dotenv").config()
const config = require("./config/web")
const logger = config.logger

const PROCESS_TYPE = process.env.NODE_PROCESS_TYPE


if (PROCESS_TYPE === "web") {
  require("./web")
  logger.log("info", "Starting %s process", PROCESS_TYPE, {pid: process.pid})
} else if (PROCESS_TYPE === "worker") {
  logger.log("info", "Starting %s process", PROCESS_TYPE, {pid: process.pid})
} else {
  throw new Error("%s is unsupported process type. Use one of web or worker", PROCESS_TYPE)
}

