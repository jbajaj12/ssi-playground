import { NextResponse } from 'next/server';
import { logMessage } from '@/lib/logger';

export async function GET() {
  logMessage('Received request: /api/chain');
  const res = await fetch('http://localhost:3000/api/slow');
  const data = await res.json();
  logMessage('Chained call completed: /api/chain -> /api/slow');
  return NextResponse.json({ message: 'Chain complete', data });
}
