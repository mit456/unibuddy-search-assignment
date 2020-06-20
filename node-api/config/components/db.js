"use strict"

require("dotenv").config()
const joi = require("joi")

const envVarsSchema = joi.object({}).unknown().required()

// To validate process.env with envVarsSchema
const {error, value: envVars} = joi.validate(process.env, envVarsSchema)

if (error) {
  throw new Error("DB validation error:", error.stack)
}

const config = {}
module.exports = config
