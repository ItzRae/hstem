import React from "react";
import { Box, Image, Text, Button, Stack } from "@chakra-ui/react";

const Result = ({ data, onOpenClick }) => {
  const { imageUrl, title, date } = data;

  return (
    <Box
      maxW="md"
      borderWidth="1px"
      borderRadius="lg"
      overflow="hidden"
      boxShadow="lg"
    >
      <Image src={imageUrl} alt={title} objectFit="cover" h="200px" />
      {/* TODO: vertical alignment, replace with Box */}
      <Stack spacing="2" p="4">
        <Text fontSize="lg" fontWeight="bold">
          {title}
        </Text>
        <Text color="gray.600">On {date}</Text>
        <Button colorScheme="purple" onClick={onOpenClick}>
          Open
        </Button>
      </Stack>
    </Box>
  );
};

export default Result;
