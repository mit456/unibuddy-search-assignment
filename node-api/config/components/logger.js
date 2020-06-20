"use strict"

require("dotenv").config()
const winston = require("winston")
const joi = require("joi")

const envVarsSchema = joi.object({
  LOGGER_LEVEL: joi.string()
    .allow(["error", "warn", "info", "verbose", "debug"])
    .default("info"),
  LOGGER_ENABLED: joi.boolean()
    .truthy("TRUE")
    .truthy("FALSE")
    .truthy("true")
    .truthy("false")
    .default(true)
}).unknown()
  .required()

// To validate process.env with envVarsSchema
const {error, value: envVars} = joi.validate(process.env, envVarsSchema)

if (error) {
  throw new Error("Logger configuration error:", error.stack)
}

let winstonLogger = winston.createLogger({
    level: envVars.LOGGER_LEVEL,
    format: winston.format.json(),
    transports: [
        //
        // - Write to all logs with level `info` and below to `combined.log`
        // - Write all logs error (and below) to `error.log`.
        //
        new winston.transports.File({ filename: "error.log", level: "error" }),
        new winston.transports.File({ filename: "combined.log" })
    ],
    exitOnError: false
})

// If we"re not in production then
// log to console
if (process.env.NODE_ENV !== "production") {
    winstonLogger.add(new winston.transports.Console({
        format: winston.format.combine(
            winston.format.splat(),
            winston.format.simple(),
            winston.format.colorize()
        )
    }));
}

const config = {
  logger: winstonLogger
  // ...
}
module.exports = config
