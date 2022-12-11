import { NextPage } from "next";
import Head from "next/head";
import { runPythonScript } from "../hooks";
import { getResponse } from "../util";

const Home: NextPage = () => (
  <>
    <Head>
      <title>Home - Nextron (with-typescript-tailwindcss)</title>
    </Head>
    <div className="grid grid-col-1 text-2xl w-full text-center">
      <img className="ml-auto mr-auto" src="/images/logo.png" />
      <span>⚡ {getResponse().response} ⚡</span>
      <span>+</span>
      <span>Next.js</span>
      <span>+</span>
      <span>tailwindcss</span>
      <span>=</span>
      <span>💕 </span>
    </div>
    <div className="mt-1 w-full flex-wrap flex justify-center">
      <button onClick={() => runPythonScript()}>
        <a className="btn-blue">Go to next page</a>
      </button>
    </div>
  </>
);

export default Home;
