import { FC, useState } from 'react';
import { getResponse } from '../../util';
import { Form } from '../common';
import { runPythonScript } from '../../hooks';

const fs = require('fs');
const writeIO = (message: string) => {
    fs.writeFileSync(
        '/Users/davidpopescu/Desktop/tmp/project-v/verity/user-input.json',
        JSON.stringify({
            user_input: message,
        })
    );
    runPythonScript();
};

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
                <Form action={() => writeIO(message)} fields={fields} />
            </div>
        </div>
    );
};

export default HomePage;
