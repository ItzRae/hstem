import React from "react";
import { Box, Image, Text, Button } from "@chakra-ui/react";

const Result = ({ data, onOpenClick }) => {
  const { imageUrl, name, major, date } = data;

  return (
    <Box
      maxW="md"
      borderWidth="1px"
      borderRadius="lg"
      overflow="hidden"
      boxShadow="lg"
    >
      <Image src={imageUrl} alt={name} objectFit="cover" h="200px" />
      <Box p="4">
        <Text fontSize="xl" fontWeight="bold" mb="2">
          {name}
        </Text>
        <Text color="gray.600" mb="2">
          {major}
        </Text>
        <Text color="gray.600" mb="2">
          On {date}
        </Text>
        <Button colorScheme="purple" onClick={onOpenClick}>
          Open
        </Button>
      </Box>
    </Box>
  );
};

export default Result;
