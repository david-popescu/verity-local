import { FC } from 'react';
import { Row } from '../types';

const Row: FC<Row> = ({ children, className }) => (
    <div
        className={
            'flex items-center justify-evenly w-full gap-3 mb-3 ' + className
        }
    >
        {children}
    </div>
);

export default Row;
