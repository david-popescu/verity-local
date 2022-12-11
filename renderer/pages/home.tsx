import { NextPage } from 'next';
import Head from 'next/head';
import { HomePage } from '../modules/pages';

const Home: NextPage = () => (
    <>
        <Head>
            <title>Home - Nextron (with-typescript-tailwindcss)</title>
        </Head>
        <HomePage />
    </>
);

export default Home;
