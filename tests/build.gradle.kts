plugins {
    kotlin("jvm") version "1.9.23"
}

group = "org.quicklybly"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

dependencies {
    implementation(kotlin("stdlib"))

    testImplementation(kotlin("test"))
    testImplementation(libs.junit)
    testImplementation(libs.selenide)
    testImplementation(libs.webDriverManager)
}

tasks.test {
    useJUnitPlatform()
}
kotlin {
    jvmToolchain(21)
}