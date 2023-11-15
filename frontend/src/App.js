import React from "react";
import { CSSReset, ChakraProvider } from "@chakra-ui/react";
import Search from "./routes/Search";

const App = () => {
  return (
    <ChakraProvider>
      <CSSReset />
      <Search />
    </ChakraProvider>
  );
};

export default App;
