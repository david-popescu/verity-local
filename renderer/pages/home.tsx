import { NextPage } from 'next';
import Head from 'next/head';
import { runPythonScript } from '../hooks';
import { getResponse } from '../util';
import { Form } from '../module/common';
import { useState } from 'react';

const Home: NextPage = () => {
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
        <>
            <Head>
                <title>Home - Nextron (with-typescript-tailwindcss)</title>
            </Head>
            <div className="mt-1 w-full flex-wrap flex justify-center">
                {/*<form action="" className="flex">*/}
                {/*    <Form fields={fields} />*/}
                {/*    <button*/}
                {/*        className="btn-blue ml-2"*/}
                {/*        onClick={() => runPythonScript()}*/}
                {/*    >*/}
                {/*        Send*/}
                {/*    </button>*/}
                {/*</form>*/}
            </div>
        </>
    );
};

export default Home;
