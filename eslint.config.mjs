import js from '@eslint/js';
import tseslint from 'typescript-eslint';

const eslintConfig = [
  js.configs.recommended,
  ...tseslint.configs.recommended,
  {
    ignores: [
      '.next/**',
      'node_modules/**',
      'out/**',
      'dist/**',
      '.cache/**',
      'public/**',
      '*.config.js',
      '*.config.mjs',
      '*.config.ts',
      'docs/**',
      'scripts/**',
    ],
  },
  {
    files: ['**/*.{ts,tsx}'],
    rules: {
      '@typescript-eslint/no-unused-vars': 'warn',
      '@typescript-eslint/no-explicit-any': 'warn',
      'react/no-unescaped-entities': 'off',
    },
  },
];

export default eslintConfig;
