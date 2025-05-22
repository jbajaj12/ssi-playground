#!/bin/bash

### This envvar injects the dd-trace module into the Node.js process before any other module.
### Recommended way to use the tracer in "Complex Frameworks usage" https://docs.datadoghq.com/tracing/trace_collection/compatibility/nodejs/#complex-framework-usage

export NODE_OPTIONS="--require dd-trace/init"
#####--------------------------------------------------------------------------#####


### Unified service tagging:

export DD_SERVICE=apm-test
export DD_ENV=apm-test
export DD_VERSION=1.0
#####--------------------------------------------------------------------------#####

### Enable the automatic span / tracer injection in the logs to correlate traces and logs. 

# export DD_LOGS_INJECTION=true
#####--------------------------------------------------------------------------#####

### Enable the debug mode to get more information about the tracer.
# export DD_TRACE_DEBUG=true

# #####--------------------------------------------------------------------------#####

# ### Enable the startup logs to get more information about the tracer.
# export DD_TRACE_STARTUP_LOGS=true

export DD_TRACE_AGENT_PORT=8136

next dev 
