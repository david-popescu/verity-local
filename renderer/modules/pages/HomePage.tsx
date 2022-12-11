import { FC, useState } from 'react';
import { getResponse } from '../../util';
import { Form } from '../common';
import { runPythonScript } from '../../hooks';

const HomePage: FC = () => {
    const [message, setMessage] = useState('');

    const fields = [
        {
            settings: {
                type: 'text',
                placeholder: 'Type anything',
                state: message,
                setState: setMessage,
                className: 'null',
            },
        },
    ];

    return (
        <div className="mt-1 w-full flex-wrap flex justify-center flex-col items-center">
            <p className="text-xl font-bold my-5">{getResponse().response}</p>
            <div className="flex">
                <Form fields={fields} />
                <button
                    className="btn-blue ml-2"
                    onClick={() => runPythonScript()}
                >
                    Send
                </button>
            </div>
        </div>
    );
};

export default HomePage;
