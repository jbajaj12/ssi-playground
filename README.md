This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.js`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.



docker run --name apm-test \
  --link dd-agent \
  -p 3001:3000 \
  -e DD_LOGS_ENABLED=true \
  -e DD_LOGS_CONFIG_CONTAINER_COLLECT_ALL=true \
  -e DD_SERVICE=apm-test-docker \
  -e DD_ENV=apm-test-docker \
  -e DD_TRACE_ENABLED=true \
  -e DD_TRACE_DEBUG=true \
  -e DD_AGENT_HOST=dd-agent \
  -e DD_LOGS_INJECTION=true \
  -e DD_GIT_COMMIT_SHA=$(git rev-parse HEAD) \
  -v $(pwd)/app.log:/app/app.log \
ccdaniele/apm-demo-app:v1


docker run -d --name dd-agent \
-e DD_API_KEY=$DD_API_KEY \
-e DD_SITE="datadoghq.com" \
-e DD_DOGSTATSD_NON_LOCAL_TRAFFIC=true \
-e DD_APM_ENABLED=true \
-e DD_APM_NON_LOCAL_TRAFFIC=true \
-e DD_APM_RECEIVER_SOCKET=/var/run/datadog/apm.socket \
-e DD_DOGSTATSD_SOCKET=/var/run/datadog/dsd.socket \
-v /var/run/datadog:/var/run/datadog \
-v /var/run/docker.sock:/var/run/docker.sock:ro \
-v /proc/:/host/proc/:ro \
-v /sys/fs/cgroup/:/host/sys/fs/cgroup:ro \
-v /var/lib/docker/containers:/var/lib/docker/containers:ro \
gcr.io/datadoghq/agent:7
