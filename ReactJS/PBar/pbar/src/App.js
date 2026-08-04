import { useEffect, useState } from "react";
import "./App.css";

const STEP = 10;
const DELAY = 100;

function App() {
  const [progress, setProgress] = useState(0);
  const [isRunning, setIsRunning] = useState(false);

  useEffect(() => {
    if (!isRunning) return;

    const intervalId = setInterval(() => {
      setProgress((prev) => Math.min(prev + STEP, 100));
    }, DELAY);

    return () => clearInterval(intervalId);
  }, [isRunning]);

  useEffect(() => {
    if (progress === 100) {
      setIsRunning(false);
    }
  }, [progress]);

  const handleStart = () => {
    if (progress < 100) {
      setIsRunning(true);
    }
  };

  const handlePause = () => {
    setIsRunning(false);
  };

  const handleReset = () => {
    setIsRunning(false);
    setProgress(0);
  };

  return (
    <div className="container">
      <h2>Progress Bar</h2>

      <div className="progress-container">
        <div
          className="progress"
          style={{ width: `${progress}%` }}
        >
          {progress}%
        </div>
      </div>

      {progress === 100 && <h3>Completed 🎉</h3>}

      <div className="buttons">
        <button onClick={handleStart} disabled={isRunning || progress === 100}>
          Start
        </button>

        <button onClick={handlePause} disabled={!isRunning}>
          Pause
        </button>

        <button onClick={handleReset} disabled={progress === 0}>
          Reset
        </button>
      </div>
    </div>
  );
}

export default App;