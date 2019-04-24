// main.go
// Accepts argument and flag input then utilizes the framework
// for building SAS Viya Docker images.
//
// Copyright 2018 SAS Institute Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     https://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package main

import (
	"fmt"
	"log"
)

func main() {
	order, err := NewSoftwareOrder()
	if err != nil {
		fmt.Println("")
		log.Fatal(err)
	}

	if order.GenerateManifestsOnly {
		err := order.GenerateManifests()
		if err != nil {
			log.Fatal(err)
		}
	} else {
		err = order.Build()
		if err != nil {
			log.Fatal(err)
		}
	}
	order.ShowSummary()
}
