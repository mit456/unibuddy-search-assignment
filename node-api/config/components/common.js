"use strict"

require("dotenv").config()
const joi = require("joi")

const envVarsSchema = joi.object({
  NODE_ENV: joi.string()
    .allow(["development", "production", "test", "provision"])
    .required()
}).unknown()
  .required()

// To validate process.env with envVarsSchema
const {error, value:envVars} = joi.validate(process.env, envVarsSchema)
if (error) {
  throw new Error("Config validation error", error.stack)
}

const config = {
  env: envVars.NODE_ENV,
  isTest: envVars.NODE_ENV === "test",
  isDevelopment: envVars.NODE_ENV === "development",
  // ....
}
module.exports = config
