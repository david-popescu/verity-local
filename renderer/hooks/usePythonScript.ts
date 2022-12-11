import { PythonShell } from 'python-shell';
import { useEffect } from 'react';

export const runPythonScript = async () => {
    await PythonShell.run(
        '/Users/davidpopescu/Desktop/tmp/project-v/verity/ai/main.py',
        null,
        (err) => {
            if (err) throw err;
        }
    );
};

const usePythonScript = () => {
    useEffect(() => {
        const foo = async () => {
            await runPythonScript();
        };
        foo();
    }, []);
};

export default usePythonScript;
