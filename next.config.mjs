/** @type {import('next').NextConfig} */
const nextConfig = {
  ...(process.env.NEXT_STATIC_EXPORT === 'true' && {
    output: 'export',
    trailingSlash: true,
  }),
  typescript: {
    ignoreBuildErrors: false,
  },
  images: {
    unoptimized: true,
  },
  ...(process.env.NEXT_STATIC_EXPORT === 'true' && {
    skipTrailingSlashRedirect: true,
  }),
};

export default nextConfig;
