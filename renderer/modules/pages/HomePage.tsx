import { FC, useState } from 'react';
import { getResponse } from '../../util';
import { Form, Box, Panel } from '../common';
import { runPythonScript } from '../../hooks';
import { Layout, Row } from '../layout';

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
    const stats = [
        {
            settings: {
                label: 'Actions',
                data: 4,
            },
        },
        {
            settings: {
                label: 'Interactions',
                data: '12K',
            },
        },
        {
            settings: {
                label: 'Correct Answers',
                data: '11.8K',
            },
        },
        {
            settings: {
                label: 'Wrong Answers',
                data: '0.2K',
            },
        },
    ];
    const panels = [
        {
            settings: {
                name: 'Activity',
                data: [
                    {
                        label: 'Mon',
                        value: '4h',
                    },
                    {
                        label: 'Tue',
                        value: '9h',
                    },
                    {
                        label: 'Wed',
                        value: '6h',
                    },
                    {
                        label: 'Thu',
                        value: '7h',
                    },
                    {
                        label: 'Fry',
                        value: '7h',
                    },
                    {
                        label: 'Sat',
                        value: '9h',
                    },
                    {
                        label: 'Sun',
                        value: '12h',
                    },
                ],
            },
        },
        {
            settings: {
                name: 'Accuracy',
                data: '98%',
            },
        },
    ];

    return (
        <Layout>
            <div className="mt-1 w-full flex-wrap flex justify-center flex-col items-center">
                <p className="text-xl font-bold my-5">
                    {getResponse().response}
                </p>
                <div className="flex w-full">
                    <Form action={() => writeIO(message)} fields={fields} />
                </div>
                <Row className="mt-5">
                    {stats.map((item, idx) => (
                        <Box key={idx} settings={item.settings} />
                    ))}
                </Row>
                <Row>
                    {panels.map((item, idx) => (
                        <Panel key={idx} settings={item.settings} />
                    ))}
                </Row>
            </div>
        </Layout>
    );
};

export default HomePage;
