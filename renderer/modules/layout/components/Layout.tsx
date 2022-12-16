import { FC } from 'react';
import { Layout } from '../types';

const Layout: FC<Layout> = ({ children, className }) => (
    <div className={'global-wrapper ' + className}>{children}</div>
);

export default Layout;
