import { FC } from 'react';
import { Field } from '../types';

const Field: FC<Field> = ({ settings }) => {
    const onChange = (e) => settings.setState(e.target.value);

    return (
        <input
            type={settings.type}
            placeholder={settings?.placeholder}
            className={
                'text-black placeholder:italic placeholder:text-slate-400 block bg-white w-full border border-slate-300 rounded-md py-2 pl-3 pr-3 shadow-sm focus:outline-none focus:border-sky-500 focus:ring-sky-500 focus:ring-1 sm:text-sm' +
                settings?.className
            }
            value={settings.state}
            onChange={onChange}
        />
    );
};

export default Field;
