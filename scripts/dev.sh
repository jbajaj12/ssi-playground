#!/bin/bash

export DD_LOGS_INJECTION=true
export DD_SERVICE=apm-test
export DD_ENV=apm-test
export DD_VERSION=1.0
export DD_GIT_REPOSITORY_URL=github.com/ccdaniele/se-ssi-playground
export DD_TRACE_AGENT_PORT=8136
export NODE_OPTIONS="--require dd-trace/init --enable-source-maps flag"
export DD_TRACE_DEBUG=true
export DD_GIT_COMMIT_SHA="525a1f1b5875367e7c12b2423527d221e1aa533c"
next dev 
