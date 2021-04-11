const wait = (ms: number) => {
  return new Promise((resolve) => {
    console.log(`please wait for ${ms} ms...`);
    setTimeout(resolve, ms);
  });
};

export default wait;
