import { ReactNode } from 'react';

export type Layout = { children: ReactNode; className?: string };
export type Row = { children: ReactNode; className?: string | null };
export type Container = { children: ReactNode; className?: string | null };
