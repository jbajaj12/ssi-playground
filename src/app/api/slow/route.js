import { NextResponse } from 'next/server';
import { logMessage } from '@/lib/logger';

export async function GET() {
  logMessage('This request will take some time as you hit the /api/slow endpoint');
  await new Promise((resolve) => setTimeout(resolve, 1000)); // Simulate delay
  logMessage('Congrats!! You just sent a request to  /api/slow');
  return NextResponse.json({ message: 'Slow response completed' });
}
