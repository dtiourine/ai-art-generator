import Image from "next/image";

export default function Home() {
    const imageString = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAACklEQVR4nGMAAQAABQABDQottAAAAABJRU5ErkJggg==";
    return (
      // <main className="flex min-h-screen items-center justify-between p-24">
      //   <div className="text-center border-amber-500 border-2 w-full max-w-5xl items-center justify-between font-mono text-sm lg:flex">
      //     <h1 className="text-4xl font-bold">
      //       Hello World
      //     </h1>
      //   </div>
      // </main>
      <main className="flex min-h-screen items-center justify-center bg-white">
          <div className="text-center border-2 border-amber-500">
              <h1 className="text-4xl font-bold">Hello World</h1>
              <Image
                  className="border-amber-500 border-2"
                  src={imageString}
                  width={500}
                  height={500}
                  alt="Tensor Image"
              />
          </div>
      </main>
  );
}
