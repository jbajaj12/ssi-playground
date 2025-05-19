import { logMessage } from '@/lib/logger';

export async function GET() {
  logMessage('Ohh!! this request failed because you just hit the /api/error endpoint');
  logMessage('About to throw intentional error');
  throw new Error('Intentional error for APM trace');
}
