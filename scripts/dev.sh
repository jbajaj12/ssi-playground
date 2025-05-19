#!/bin/bash

export DD_LOGS_INJECTION=true
export DD_SERVICE=apm-test
export DD_GIT_REPOSITORY_URL=github.com/ccdaniele/se-ssi-playground
export DD_TRACE_AGENT_PORT=8136
export DD_ENV=apm-test
export NODE_OPTIONS="--require dd-trace/init"
export DD_TRACE_DEBUG=true

next dev
