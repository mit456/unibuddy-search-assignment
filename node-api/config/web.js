'use strict'

const common = require('./components/common')
const logger = require('./components/logger')
const server = require('./components/server')
const db = require('./components/db')


module.exports = Object.assign({}, common, logger, server, db)
