import { FC } from 'react';
import { Box } from '../types';

const Box: FC<Box> = ({ settings }) => {
    return (
        <div className="w-full text-center p-5 border-2 rounded bg-white">
            <p className="text-5xl font-bold">{settings.data}</p>
            <p className="text-lg">{settings.label}</p>
        </div>
    );
};

export default Box;
