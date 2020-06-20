"use strict"

require("dotenv").config()
const joi = require("joi")

const envVarsSchema = joi.object({
  PORT: joi.number()
    .required()
}).unknown()
  .required()


// To validate process.env with envVarsSchema
const {error, value:envVars} = joi.validate(process.env, envVarsSchema)
if (error) {
  throw new Error("Server config validation error:", error.stack)
}

const config = {
  server: {
    port: envVars.PORT
  }
}

module.exports = config
