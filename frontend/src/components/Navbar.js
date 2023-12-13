import React from "react";
import { Link } from "react-router-dom";
import { Box, Flex, Spacer, Heading, Text } from "@chakra-ui/react";
import SearchBar from "./SearchBar";

const Navbar = ({ onSearch }) => {
  return (
    <Box bg="purple.500" p="4" color="white">
      <Flex alignItems="center">
        <Heading as="h1" size="lg">
          HStem DB
        </Heading>
        <Spacer />
        <Box>
          <Link to="/" mr="4">
            Home
          </Link>
          <Link to="/admin">Admin</Link>
        </Box>
      </Flex>
    </Box>
  );
};

export default Navbar;