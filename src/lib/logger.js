import winston from 'winston';
import tracer from 'dd-trace';

// Initialize dd-trace (guard to prevent duplicate init)
if (!tracer._tracing) {
  tracer.init({
    logInjection: true, // Enable automatic trace/span injection
  });
}

// Create a Winston logger that writes to app.log
const logger = winston.createLogger({
  level: 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.printf(({ timestamp, level, message }) => {
      // Inject trace ID and span ID manually if available
      const span = tracer.scope().active();
      const traceId = span?.context()?.toTraceId?.() || 'N/A';
      const spanId = span?.context()?.toSpanId?.() || 'N/A';
      return `[${timestamp}] [${level}] [dd.trace_id=${traceId} dd.span_id=${spanId}] ${message}`;
    })
  ),
  transports: [
    new winston.transports.File({ filename: 'app.log' }),
  ],
});

export function logMessage(message) {
  logger.info(message);
}




// import fs from 'fs';
// import path from 'path';

// const logFile = path.join(process.cwd(), 'app.log');

// export function logMessage(message) {
//   const timestamp = new Date().toISOString();
//   const logLine = `[${timestamp}] ${message}\n`;
//   fs.appendFileSync(logFile, logLine);
// }
