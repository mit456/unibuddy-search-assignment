"use strict"

const config = require("../config/web")
const logger = config.logger

const express = require("express")
const bodyParser = require("body-parser")
const helmet = require("helmet")
const nodeLimits = require("limits")
const path = require("path")

const reqDuration = 2629746000;

// Main function starts node API server at
// PORT set in config
async function main() {
    try {
        const app = express();
        app.use(bodyParser.json({
            limit: "1mb" // Limit string length
        }));

        app.use(bodyParser.urlencoded({
            extended: true
        }));

        // Security by obsecurity (helmet does this)
        app.disable("x-powered-by");

        // use helmet
        app.use(helmet())

        // hsts
        app.use(helmet.hsts({
          maxAge: reqDuration
        }));

        // Framebuster
        app.use(helmet.frameguard({
          action: "deny"
        }));

        // Content security policy
        app.use(helmet.contentSecurityPolicy({
          directives: {
            defaultSrc: ["'self'"],
            scriptSrc: ["'self'"],
            childSrc: ["'none'"],
            objectSrc: ["'none'"],
            formAction: ["'none'"]
          }
        }));

        // x-xss protection
        app.use(helmet.xssFilter());

        // x-content-type-options
        app.use(helmet.noSniff());

        // Limit somethings
        app.use(nodeLimits({
          file_uploads: true,
          post_max_size: 100000, // 1 mb max upload
          inc_req_timeout: 1000 * 60 // 60 Seconds
        }));

        // Port from config
        const port = config["server"]["port"]
        await app.get("/", function(req, res) {
          res.send("Hello World");
        })

        app.listen(port, function () {
          logger.log("info", "Express listening on port %d", port);
        })

        // Setup routes
        require(".")(app)
        return app;
    } catch (error) {
        logger.log("error", "Error: App start %s", error)
    }
}

main()
