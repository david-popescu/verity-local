import { FC, Fragment } from 'react';
import { Panel } from '../types';
import { isArray } from 'util';

const Panel: FC<Panel> = ({ settings }) => {
    return (
        <div className="w-full text-center p-5 border-2 rounded bg-white">
            {isArray(settings.data) ? (
                settings.data.map((item, idx) => (
                    <Fragment key={idx}>
                        <p>{item.value}</p>
                        <p>{item.label}</p>
                    </Fragment>
                ))
            ) : (
                <p>{settings.data}</p>
            )}
            <p className="text-lg">{settings.name}</p>
        </div>
    );
};

export default Panel;
